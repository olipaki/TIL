import axios from "axios";
import React, { useEffect, useState } from "react";

const ProductsSort = () => {
  const [product, setProducts] = useState([]);
  const [options, setOptions] = useState({
    sortBy: "price",
    order: "asc",
  });

  useEffect(() => {
    const fetchProducts = async () => {
      const { sortBy, order } = options;

      const response = await axios.get(
        `https://dummyjson.com/products?sortBy=${sortBy}&order=${order}`,
      );
      //   console.log(response.data);
      const data = response.data;
      setProducts(data.products);
    };

    fetchProducts();
  }, [options.sortBy, options.order]);

  return (
    <div className="card">
      <div>ProductsSort</div>
      <div>
        {/* <button
          className="button"
          onClick={() => setOptions({ sortBy: "id", order: "asc" })}
        >
          ID 오름
        </button>
        <button
          className="button"
          onClick={() => setOptions({ sortBy: "id", order: "desc" })}
        >
          ID 내림
        </button>
        <button
          className="button"
          onClick={() => setOptions({ sortBy: "price", order: "asc" })}
        >
          price 오름
        </button>
        <button
          className="button"
          onClick={() => setOptions({ sortBy: "price", order: "desc" })}
        >
          price 내림
        </button>
        <button
          className="button"
          onClick={() => setOptions({ sortBy: "rating", order: "asc" })}
        >
          rating 오름
        </button>
        <button
          className="button"
          onClick={() => setOptions({ sortBy: "rating", order: "desc" })}
        >
          rating 내림
        </button> */}

        {/* 만약에 보이는 것을 다르게 하고 싶다면 아래의 array를 object로 만들어서
        {
            value : 'id',
            represent : '아이디'
        }

        형식으로 사용 가능.
        */}
        {["id", "price", "rating"].map((el) => {
          return (
            <div key={el}>
              {["asc", "desc"].map((dirction) => {
                return (
                  <button
                    className={`button ${
                      options.sortBy === el &&
                      options.order === dirction &&
                      "bg-blue-400"
                    }`}
                    onClick={() => setOptions({ sortBy: el, order: dirction })}
                    key={dirction}
                  >
                    {el} {dirction}
                  </button>
                );
              })}
            </div>
          );
        })}
      </div>
      <div>
        {product.map((product) => {
          return (
            <div className="card" key={product.id}>
              <div>id : {product.id}</div>
              <div>title : {product.title}</div>
              <div>price : {product.price}</div>
              <div>rating : {product.rating}</div>
            </div>
          );
        })}
      </div>
    </div>
  );
};

export default ProductsSort;
