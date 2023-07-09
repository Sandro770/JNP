import React, {useEffect} from 'react';
import {Product} from "../interfaces/product"

const Products = () => {

    const [products, setProducts] = React.useState([]);

    useEffect(() => {
        (async () => {
            const response = await fetch('http://localhost:8000/api/products');
            const data = await response.json();
            setProducts(data);
            console.log(data);
        })();

    }, []);

    const del = async (id: number) => {
        if (!window.confirm('Are you sure you want to delete this product?')) {
            await fetch(`http://localhost:8000/api/products/${id}`, {
                    method: 'DELETE'
                }
            );
            setProducts(products.filter((p: Product) => p.id !== id));
        }
    }

    return (
        <div>
            <h2>Section title</h2>
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
                                        <a className="btn btn-sm btn-outline-secondary"
                                           onClick={() => del(p.id)}>Delete</a>
                                    </div>
                                </td>
                            </tr>
                        )
                    })}
                    </tbody>
                </table>
            </div>
        </div>
    );
};

export default Products;