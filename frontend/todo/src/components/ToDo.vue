<template>
       <div>
           <form>
            <input placeholder="Enter todo list name"
                v-model="name"
                class="input is-small" text="text" />
            <input placeholder="Enter todo list decription"
                v-model="description"
                class="input is-small" text="text" />
            <button type="submit" class="btn btn-primary"
                @click="addTodoList()">Submit</button>
           </form>

           <form @submit="submitForm">
                <div class="row">
                    <div class="col">
                    <input ref="name" type="text" class="form-control" placeholder="First name">
                    </div>
                    <div class="col">
                    <input ref="description" type="text" class="form-control" placeholder="Last name">
                    </div>
                </div>
            </form>
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
        addTodoList(evt) {
            evt.preventDefault();
            let name = this.$ref.name.value;
            let description = this.$ref.description.value;
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