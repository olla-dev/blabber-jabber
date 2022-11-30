import UserList from '../components/UserList'

const dummy_users = [
  { 
    first_name: "John", 
    last_name:"Doe",
    username: "jdoe",
    profile: { 
      bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.",
      online: true 
    } 
  },
  { 
    first_name: "George", 
    last_name:"Stinson",
    username: "gstinson",
    profile: { 
      bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.",
      online: false 
    } 
  },
  { 
    first_name: "Susan", 
    last_name:"Jasper",
    username: "sjasper",
    profile: { 
      bio: "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Proin ornare magna eros, eu pellentesque tortor vestibulum ut. Maecenas non massa sem. Etiam finibus odio quis feugiat facilisis.",
      online: true 
    } 
  },
]

// More on default export: https://storybook.js.org/docs/vue/writing-stories/introduction#default-export
export default {
  title: 'Chat/UserList',
  component: UserList,
  // More on argTypes: https://storybook.js.org/docs/vue/api/argtypes
  argTypes: {
    users: dummy_users,
    isLoading: false
  },
};

// More on component templates: https://storybook.js.org/docs/vue/writing-stories/introduction#using-args
const Template = (args) => ({
  // Components used in your story `template` are defined in the `components` object
  components: { UserList },
  // The story's `args` need to be mapped into the template through the `setup()` method
  setup() {
    return { args };
  },
  // And then the `args` are bound to your component with `v-bind="args"`
  template: '<user-list v-bind="args" />',
});

export const Loaded = Template.bind({});
// More on args: https://storybook.js.org/docs/vue/writing-stories/args
Loaded.args = {
  users: dummy_users,
  isLoading: false
};