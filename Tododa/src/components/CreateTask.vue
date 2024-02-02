<template>
  <div class="inputarea">
    <div class="text">
      <input type="text" placeholder="Нужно просто начать" v-model="txt" />
    </div>

    <div class="tag">
      <input type="text" placeholder="Добавьте тэг" v-model="tag" />
    </div>
    <div>
      <button type="button" @click="taskcreate">
        <img src="../assets/plus.svg" draggable="false" />
      </button>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      txt: '',
      tag: '',
    }
  },

  methods: {
    taskcreate() {
      let trimedtxt = this.txt.trim()
      let trimedtag = this.tag.trim()
      if (trimedtxt !== '') {
        if (trimedtag === '') {
          trimedtag = 'Без тэга'
        }
        this.$emit('addtask', { text: trimedtxt, tag: trimedtag, done: false })

        this.txt = ''
        this.tag = ''
      }
    },
  },
};
</script>

<style scoped>
.inputarea {
  display: flex;
  align-items: center;
  justify-content: space-between;
  margin: 20px 0px;
  padding: 20px;
  background-color: var(--block-bg);
  border-radius: 15px;
}

.text {
  width: 55%;
}

.tag {
  width: 25%;
}

.inputarea input {
  width: 100%;
  font-size: 1.5rem;
  padding: 10px 20px;
  border-radius: 10px;
  border: none;
}

.inputarea button {
  background-color: rgb(126, 187, 240);
}

.inputarea button:hover {
  background-color: rgb(88, 170, 242);
}

.inputarea button:active {
  scale: 0.95;
}
</style>