import express from 'express';
import { createClient } from 'redis';

const client = createClient();

const listProducts = [
    { id: 1, name: 'Suitcase 250', price: 50, stock: 4 },
    { id: 2, name: 'Suitcase 450', price: 100, stock: 10 },
    { id: 3, name: 'Suitcase 650', price: 350, stock: 2 },
    { id: 4, name: 'Suitcase 1050', price: 550, stock: 5 }
];

const getItemById = (id) => listProducts.find(product => product.id === id);


client.on('error', (err) => console.error('Redis Client Error', err));
client.connect();

const reserveStockById = (itemId, stock) => {
    client.set(`item.${itemId}`, stock);
};

const getCurrentReservedStockById = async (itemId) => {
    const stock = await client.get(`item.${itemId}`);
    return stock;
};


const app = express()

app.listen(1245)

app.get('/list_products', (res, req) => {
    const formattedProducts = listProducts.map(product => ({
        itemId: product.id,
        itemName: product.name,
        price: product.price,
        initialAvailableQuantity: product.stock
    }));

    res.json(formattedProducts);
})

app.get('GET /list_products/:itemId', (res, req) => {
    const id = req.params.itemId;
    const product = listProducts.find(product => product.id === id);
    if (!product)
        res.json({"status":"Product not found"});
    const formattedProduct = {"itemId": product.id, "itemName": product.name, "price": product.price, initialAvailableQuantity: product.stock, currentQuantity: product.stock}
    res.json(formattedProduct);
})


export default {listProducts, getItemById, app};
