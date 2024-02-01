<template>
    <div>
        <span>#</span><span>{{ tag }}</span>
    </div>
</template>
  
<script>
export default {
    props: {
        tag: {
            type: String,
            required: true,
        },
    },
};
</script>

<style scoped>
span{
    font-size: 1.3rem;
    color: black;
}

div{
    display: flex;
    flex-wrap: wrap;
    width: fit-content;
    padding: 10px;
    border-radius: 10px;
    background-color: rgba(0, 0, 0, 0.162);
}
</style>