import UserTyping from '../components/UserTyping'

// More on default export: https://storybook.js.org/docs/vue/writing-stories/introduction#default-export
export default {
  title: 'Chat/UserTyping',
  component: UserTyping,
  // More on argTypes: https://storybook.js.org/docs/vue/api/argtypes
  argTypes: {
    user: { 
      first_name: "John", 
      last_name:"Doe"
    },
  },
};

// More on component templates: https://storybook.js.org/docs/vue/writing-stories/introduction#using-args
const Template = (args) => ({
  // Components used in your story `template` are defined in the `components` object
  components: { UserTyping },
  // The story's `args` need to be mapped into the template through the `setup()` method
  setup() {
    return { args };
  },
  // And then the `args` are bound to your component with `v-bind="args"`
  template: '<user-typing v-bind="args" />',
});

export const Typing = Template.bind({});
// More on args: https://storybook.js.org/docs/vue/writing-stories/args
Typing.args = {
    user: { 
      first_name: "John", 
      last_name:"Doe"
    }
};