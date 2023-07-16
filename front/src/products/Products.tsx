import React, { useEffect, useState } from 'react';
import { Product } from '../interfaces/product';

interface FormValues {
  name: string;
  quantity: string;
  price: string;
}

const Products: React.FC = () => {
  const [products, setProducts] = useState<Product[]>([]);
  const [formValues, setFormValues] = useState<FormValues>({
    name: '',
    quantity: '',
    price: ''
  });

  useEffect(() => {
    (async () => {
      const response = await fetch('http://0.0.0.0:8000/api/products');
      const data = await response.json();
      setProducts(data);
      console.log(data);
    })();
  }, []);

  const del = async (id: number) => {
    if (window.confirm('Are you sure you want to delete this product?')) {
        await fetch(`http://0.0.0.0:8000/api/products/${id}`, {
        method: 'DELETE'
      });
      setProducts(products.filter((p: Product) => p.id !== id));
    }
  };

  const handleFormChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    const { name, value } = event.target;
    setFormValues((prevValues) => ({ ...prevValues, [name]: value }));
  };

  const handleFormSubmit = async (event: React.FormEvent<HTMLFormElement>) => {
    event.preventDefault();

    try {
      const response = await fetch('http://0.0.0.0:8000/api/products', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(formValues)
      });

      if (response.ok) {
        const data = await response.json();
        setProducts((prevProducts) => [...prevProducts, data]);
        console.log('POST request successful');
      } else {
        console.error('POST request failed');
      }
    } catch (error) {
      console.error('Error occurred:', error);
    }
  };

  return (
    <div>
      <h2>Section title</h2>

      {/* Form Component */}
      <form onSubmit={handleFormSubmit}>
        <div>
          <label htmlFor="name">Name:</label>
          <input
            type="text"
            id="name"
            name="name"
            value={formValues.name}
            onChange={handleFormChange}
          />
        </div>
        <div>
          <label htmlFor="quantity">Quantity:</label>
          <input
            type="text"
            id="quantity"
            name="quantity"
            value={formValues.quantity}
            onChange={handleFormChange}
          />
        </div>
        <div>
          <label htmlFor="price">Price:</label>
          <input
            type="text"
            id="price"
            name="price"
            value={formValues.price}
            onChange={handleFormChange}
          />
        </div>
        <button type="submit">Add Product</button>
      </form>

      {/* Products Table */}
      <div className="table-responsive small">
        <table className="table table-striped table-sm">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">Name</th>
              <th scope="col">Owner</th>
              <th scope="col">Quantity</th>
              <th scope="col">Price</th>
              <th scope="col">Action</th>
            </tr>
          </thead>
          <tbody>
            {products.map((p: Product) => {
              return (
                <tr key={p.id}>
                  <td>{p.id}</td>
                  <td>{p.name}</td>
                  <td>{p.owner}</td>
                  <td>{p.quantity}</td>
                  <td>{p.price}</td>
                  <td>
                    <div className="btn-group mr-2">
                      <a className="btn btn-sm btn-outline-secondary" onClick={() => del(p.id)}>
                        Delete
                      </a>
                    </div>
                  </td>
                </tr>
              );
            })}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Products;
