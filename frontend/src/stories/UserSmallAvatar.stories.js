import UserSmallAvatar from '../components/UserSmallAvatar'

// More on default export: https://storybook.js.org/docs/vue/writing-stories/introduction#default-export
export default {
  title: 'Chat/UserSmallAvatar',
  component: UserSmallAvatar,
  // More on argTypes: https://storybook.js.org/docs/vue/api/argtypes
  argTypes: {
    user: { profile: { online: true } },
  },
};

// More on component templates: https://storybook.js.org/docs/vue/writing-stories/introduction#using-args
const Template = (args) => ({
  // Components used in your story `template` are defined in the `components` object
  components: { UserSmallAvatar },
  // The story's `args` need to be mapped into the template through the `setup()` method
  setup() {
    return { args };
  },
  // And then the `args` are bound to your component with `v-bind="args"`
  template: '<user-small-avatar v-bind="args" />',
});

export const Online = Template.bind({});
// More on args: https://storybook.js.org/docs/vue/writing-stories/args
Online.args = {
  user: {
    profile: {
      online: true
    }
  }
};
export const Offline = Template.bind({});
// More on args: https://storybook.js.org/docs/vue/writing-stories/args
Offline.args = {
  user: {
    profile: {
      online: false
    }
  }
};



