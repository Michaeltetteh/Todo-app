<template>
       <div>
            <input placeholder="Enter todo list name"
                v-model="input"
                class="input is-small" text="text" />
            <input placeholder="Enter todo list decription"
                v-model="input"
                class="input is-small" text="text" />
            <button type="submit" class="btn btn-primary">Submit</button>
       </div>
</template>

<script>
export default {
    name: "ToDo"
}
</script>

<style scoped>

</style>