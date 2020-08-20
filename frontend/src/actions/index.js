
export const loadRevenueData = userId => (dispatch, getState) => {
  fetch(`http://localhost:8000/revenue/${userId}`)
    .then(d => d.json())
    .then(d => dispatch({
      type: 'LOAD_REVENUE_DATA',
      userId,
      data: d
    }));
};

// export const loadRevenueData = (userId) => (dispatch, getState) => {
//   let data = {};
//   if (userId === 2) {
//     data = {
//       revenue: [
//         {
//           name: 'Akeel Peters',
//           revenue: '17248.65',
//         },
//         {
//           name: 'Faye Finch',
//           revenue: '18372.40',
//         },
//         {
//           name: 'Tasmin Tyson',
//           revenue: '19360.15',
//         },
//         {
//           name: 'Rhiana Fitzgerald',
//           revenue: '17545.55',
//         },
//         {
//           name: 'Gracie Byers',
//           revenue: '15647.60',
//         },
//       ],
//     };
//   }
//   if (userId === 32) {

      
//     data = {
//       revenue: [
//         {
//           name: 'John',
//           revenue: '12384.23',
//         },
//         {
//           name: 'Smith',
//           revenue: '94785.34',
//         },
//         {
//           name: 'Adam',
//           revenue: '18473.86',
//         },
//         {
//           name: 'Josh',
//           revenue: '49058.23',
//         },
//         {
//           name: 'Doe',
//           revenue: '48634.45',
//         },
//       ],
//     };
//   }
//   if (userId === 203) {
//     data = {
//       revenue: [
//         {
//           name: 'John',
//           revenue: '47546.23',
//         },
//         {
//           name: 'Smith',
//           revenue: '74634.09',
//         },
//         {
//           name: 'Adam',
//           revenue: '23546.21',
//         },
//         {
//           name: 'Josh',
//           revenue: '39421.34',
//         },
//         {
//           name: 'Doe',
//           revenue: '98272.23',
//         },
//       ],
//     };
//   }
//   dispatch({
//     type: 'LOAD_REVENUE_DATA',
//     userId,
//     data,
//   });
//   // fetch(`http://localhost:8000/revenue/${userId}`)
//   //   .then((d) => d.json())
//   //   .then((d) =>
//   //     dispatch({
//   //       type: 'LOAD_REVENUE_DATA',
//   //       userId,
//   //       data: d.revenue,
//   //     })
//   //   );
// };
