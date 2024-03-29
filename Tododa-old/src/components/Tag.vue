<template>
    <div>
        # {{ tag }}
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
div{
    display: flex;
    flex-wrap: nowrap;
    padding: 10px;
    border-radius: 10px;
    margin: 10px 20px;
    text-wrap: nowrap;
}
</style>