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
    flex-wrap: wrap;
    padding: 10px;
    border-radius: 10px;
    margin: 0px 20px;
}
</style>