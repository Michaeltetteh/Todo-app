<template>
       <div>
            <input placeholder="Enter todo list name"
                v-model="name"
                class="input is-small" text="text" />
            <input placeholder="Enter todo list decription"
                v-model="description"
                class="input is-small" text="text" />
            <button type="submit" class="btn btn-primary"
                @click="addTodoList()">Submit</button>
       </div>
</template>

<script>
import { mapActions } from 'vuex';
export default {
    name: "ToDo",
    data() {
        return {
            name: '',
            description: ''
        }
    },

    methods: {
        addTodoList() {
            let name = this.name;
            let description = this.description;
            this.$store.dispatch('addTodoList',{'name':name,'description':description});
            this.name = '';
            this.description = '';  
        }
    },
    updated: {
        ...mapActions([
        'getTodoItems'
        ])
    }  
}
</script>

<style scoped>

</style>