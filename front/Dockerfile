# Use the official Node.js 14 base image
FROM node:14

# Set the working directory
WORKDIR /app

# Copy package.json and package-lock.json to the container
COPY package*.json ./

# Install dependencies
RUN npm install -g create-react-app
RUN npm install react-scripts
RUN npm install react-router-dom @types/react-router-dom

# Copy the rest of the application code to the container
COPY . .

# Expose port 3000
EXPOSE 3000

# Start the React app
CMD ["npm", "start"]
