var Home = React.createClass({
  componentDidMount: function() {
    componentHandler.upgradeDom();
  },

  render: function() {
    return (
      <div>
        Home
      </div>
    )
  }
})

bottlereact._register('Home', Home)
