<template>
    <div class="order">
        <div class="number">
            <span>{{ number }}</span>
        </div>

        <div class="createdate">
            <span> {{ createdate }}</span>
        </div>

        <div class="status">
            <span> {{ status }}</span>
        </div>

        <div class="comment">
            <span> {{ comment }}</span>
        </div>

        <div class="count">
            <span> {{ count }}</span>
        </div>

        <div class="price">
            <span> {{ price }}</span>
        </div>

        <div class="action">
            <span><button type="button">action</button></span>
        </div>
    </div>
</template>

<script setup>
defineProps({
    number: String,
    status: String,
    comment: String,
    price: Number,
    createdate: String,
    count: Number
})
</script>

<style scoped>
.order {
    display: flex;
    width: 100%;
    min-width: 1200px;
}

.order>div {
    width: 100%;
    text-align: center;
    text-wrap: nowrap;
    padding: 10px 20px;
    font-weight: 500;
}

.number {
    max-width: 150px;
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
    max-width: 170px;
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
</style>