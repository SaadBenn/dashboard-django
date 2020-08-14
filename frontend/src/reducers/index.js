
const initialState = {
  revenue: {},
};

export const reducer = (state = initialState, action) => {
  if (action.type === 'LOAD_REVENUE_DATA'){
    return Object.assign({}, state, {
      revenue: Object.assign({}, state.revenue,
        { [action.userId]: action.data }
      )
    });
  }
  return state;
};
