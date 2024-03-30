<template>
    <div class="table">
      <div class="table-navbar">
        <div class="number">
          <span @click="sortOrders('number')">№</span>
          <img
            class="arrow"
            src="./assets/caret-up-fill.svg"
            alt=""
            :class="{ 'arrow-up': sortState.sortBy === 'number' && !sortState.sortAscending, 'arrow-down': sortState.sortBy === 'number' && !sortState.sortAscending }"
            v-show="sortState.sortBy === 'number'"
          />
        </div>
        <div class="createdate">
          <span>Дата создания</span>
        </div>
  
        <div class="status">
          <span>Статус</span>
        </div>
  
        <div class="comment">
          <span>Комментарий к заказу</span>
        </div>
  
        <div class="count">
          <span @click="sortOrders('amount')">Кол-во позиций</span>
          <img
            class="arrow"
            src="./assets/caret-up-fill.svg"
            alt=""
            :class="{ 'arrow-up': sortState.sortBy === 'amount' && !sortState.sortAscending, 'arrow-down': sortState.sortBy === 'amount' && !sortState.sortAscending }"
            v-show="sortState.sortBy === 'amount'"
          />
        </div>
  
        <div class="price">
          <span @click="sortOrders('price')">Сумма</span>
          <img
            class="arrow"
            src="./assets/caret-up-fill.svg"
            alt=""
            :class="{ 'arrow-up': sortState.sortBy === 'price' && !sortState.sortAscending, 'arrow-down': sortState.sortBy === 'price' && !sortState.sortAscending }"
            v-show="sortState.sortBy === 'price'"
          />
        </div>
  
        <div class="action">
          <span>Действия</span>
        </div>
      </div>
  
      <div class="order-wrapper">
        <Order
          v-for="order in paginatedOrders"
          :key="order.number"
          :number="order.number"
          :createdate="order.created_at"
          :status="order.status"
          :comment="order.comment"
          :count="order.amount"
          :price="order.price"
        />
      </div>
    </div>

    <div class="bottom-content">
        <select name="orderscount" id="" v-model="orderscount">
          <option value="5">5</option>
          <option value="10">10</option>
          <option value="15">15</option>
          <option value="20">20</option>
        </select>
        
        <div class="pagination">
          <button class="prev" @click="prevPage" :disabled="currentPage === 1"><img src="./assets/caret-up-fill.svg" alt=""></button>
          <span>Страница {{ currentPage }} из {{ totalPages }}</span>
          <button class="next" @click="nextPage" :disabled="currentPage === totalPages"><img src="./assets/caret-up-fill.svg" alt=""></button>
        </div>
    </div>
  
  
  </template>
  
  <script setup>
  import Order from './assets/components/Order.vue';
  import { ref, reactive, computed, watch } from "vue";
  
  let allorders = ref([
    {
        "number": "S4157595",
        "status": "В архиве",
        "price": 200,
        "created_at": "16.01.2023",
        "amount": 5
    },
    {
        "number": "S3857573",
        "status": "В работе",
        "price": 9678,
        "created_at": "09.01.2024",
        "amount": 2
    },
    {
        "number": "S3657591",
        "status": "В архиве",
        "price": 1355,
        "created_at": "01.01.2024",
        "amount": 6
    },
    {
        "number": "S3457598",
        "status": "Выполнен",
        "price": 200,
        "created_at": "09.01.2024",
        "amount": 1
    },
    {
        "number": "S3357595",
        "status": "В работе",
        "price": 233,
        "created_at": "09.01.2023",
        "amount": 6
    },
    {
        "number": "S3257598",
        "status": "В работе",
        "price": 2855,
        "created_at": "09.01.2024",
        "amount": 3
    },
    {
        "number": "S3157695",
        "status": "В архиве",
        "price": 1744,
        "created_at": "09.01.2023",
        "amount": 1
    },
    {
        "number": "S3157595",
        "status": "Выполнен",
        "price": 3685,
        "created_at": "09.01.2024",
        "amount": 3
    },
    {
        "number": "S3157592",
        "status": "Выполнен",
        "price": 6584,
        "created_at": "09.01.2024",
        "amount": 1
    },
    {
        "number": "S3157564",
        "status": "В архиве",
        "price": 6978,
        "created_at": "09.01.2023",
        "amount": 4
    },
    {
        "number": "S3157533",
        "status": "В архиве",
        "price": 3644,
        "created_at": "01.04.2023",
        "amount": 7
    },
    {
        "number": "S3157514",
        "status": "В архиве",
        "price": 9722,
        "created_at": "09.01.2024",
        "amount": 8
    },
    {
        "number": "S3151522",
        "status": "В работе",
        "price": 69858,
        "created_at": "09.01.2024",
        "amount": 6
    },
    {
        "number": "S4157595",
        "status": "В архиве",
        "price": 200,
        "created_at": "16.01.2023",
        "amount": 5
    },
    {
        "number": "S3857573",
        "status": "В работе",
        "price": 9678,
        "created_at": "09.01.2024",
        "amount": 2
    },
    {
        "number": "S3657591",
        "status": "В архиве",
        "price": 1355,
        "created_at": "01.01.2024",
        "amount": 6
    },
    {
        "number": "S3457598",
        "status": "Выполнен",
        "price": 200,
        "created_at": "09.01.2024",
        "amount": 1
    },
    {
        "number": "S3357595",
        "status": "В работе",
        "price": 233,
        "created_at": "09.01.2023",
        "amount": 6
    },
    {
        "number": "S3257598",
        "status": "В работе",
        "price": 2855,
        "created_at": "09.01.2024",
        "amount": 3
    },
    {
        "number": "S3157695",
        "status": "В архиве",
        "price": 1744,
        "created_at": "09.01.2023",
        "amount": 1
    }
]);

let orderscount = ref(5);
let currentPage = ref(1);

const sortState = reactive({
  sortBy: null,
  sortAscending: true
});

watch(orderscount, (newValue) => {
  const totalPagesAfterChange = Math.ceil(allorders.value.length / newValue);
  totalPages.value = totalPagesAfterChange;

  // Проверяем, остается ли текущая страница в пределах доступных страниц
  currentPage.value = Math.min(currentPage.value, totalPagesAfterChange);

  // Обновляем paginatedOrders
  updatePaginatedOrders();
});

const updatePaginatedOrders = () => {
  const startIndex = (currentPage.value - 1) * orderscount.value;
  const endIndex = Math.min(startIndex + orderscount.value, allorders.value.length);
  paginatedOrders.value = allorders.value.slice(startIndex, endIndex);
};

const setCurrentPage = (value) => {
  const totalPagesAfterChange = Math.ceil(allorders.value.length / orderscount.value);
  currentPage.value = Math.min(Math.max(1, value), totalPagesAfterChange);
  updatePaginatedOrders();
};

const nextPage = () => {
  setCurrentPage(currentPage.value + 1);
};

const prevPage = () => {
  setCurrentPage(currentPage.value - 1);
};

const sortOrders = (sortBy) => {
  if (sortState.sortBy === sortBy) {
    sortState.sortAscending = !sortState.sortAscending;
  } else {
    sortState.sortBy = sortBy;
    sortState.sortAscending = true;
  }

  const { sortAscending } = sortState;

  paginatedOrders.value.sort((a, b) => {
    const valueA = a[sortBy];
    const valueB = b[sortBy];

    if (typeof valueA === 'string' && typeof valueB === 'string') {
      return sortAscending ? valueA.localeCompare(valueB) : valueB.localeCompare(valueA);
    } else {
      return sortAscending ? valueA - valueB : valueB - valueA;
    }
  });
};

watch(currentPage, () => {
  updatePaginatedOrders();
});

const totalPages = computed(() => Math.ceil(allorders.value.length / orderscount.value));

const paginatedOrders = ref([]);

// Инициализация paginatedOrders
updatePaginatedOrders();
</script>  
<style scoped>
* {
    padding: 0;
    margin: 0;
}

body {
    padding: 50px;
}

.table {
    overflow-x: auto;
    border: 2px solid rgba(0, 0, 0, 0.3);
    border-radius: 10px;
}

.table-navbar,
.order {
    display: flex;
    width: 100%;
    min-width: 1200px;
}

.table-navbar {
    background-color: rgba(0, 0, 0, 0.2);

}

.table-navbar>div {
    width: 100%;
    text-align: center;
    text-wrap: nowrap;
    padding: 10px 20px;
    font-weight: 500;

    display: flex;
    justify-content: center;
    align-items: center;
}

.number {
    max-width: 180px;
}

.createdate {
    max-width: 150px;
}

.status {
    max-width: 140px;
}

.comment {
    min-width: 400px;
}

.count {
    max-width: 200px;
}

.price {
    max-width: 100px;
}

.action {
    max-width: 100px;
}

.order-wrapper {
    padding: 20px 0px;
}

.arrow {
    transition: all 0.5s ease;
    padding: 0px 5px;
}

.arrow-up {
    transform: rotate(0deg);
}

.arrow-down {
    transform: rotate(180deg);
}

.bottom-content{
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 10px;
}

.bottom-content .pagination button{
    margin: 0px 10px;
    padding: 5px;
    width: 30px;
    height: 30px;
}

select{
    text-align: center;
    font-size: 1.2rem;
    padding: 10px;
}

.pagination .prev img{
    transform: rotate(-90deg);
}

.pagination .next img{
    transform: rotate(90deg);
}

</style>
