
export const loadRevenueData = userId => (dispatch, getState) => {
  fetch(`http://localhost:8000/revenue/${userId}`)
    .then(d => d.json())
    .then(d => dispatch({
      type: 'LOAD_REVENUE_DATA',
      userId,
      data: d
    }));
};
