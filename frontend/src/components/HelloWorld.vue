<template>
  <div class="hello">
    <h1>{{ result }}</h1>
    <p>
      For a guide and recipes on how to configure / customize this project,<br />
      check out the
      <a href="https://cli.vuejs.org" target="_blank" rel="noopener"> vue-cli documentation</a>.
    </p>
    <div>
      <input v-model="name" />
      <button @click="submit">Submit</button>
    </div>
  </div>
</template>

<script>
export default {
  name: "HelloWorld",
  data: () => ({
    name: "Prime Labo",
    result: "",
  }),
  methods: {
    async submit() {
      const response = await fetch(`/api/index/?name=${encodeURIComponent(this.name)}`);
      const data = await response.json();
      this.result = data.content;
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
