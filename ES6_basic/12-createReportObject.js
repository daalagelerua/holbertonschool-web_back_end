export default function createReportObject(employeesList) {
    const allEmployees = { ...employeesList }; // Using spread syntax to clone the employeesList
  
    return {
        allEmployees, // Assigning the allEmployees object
        getNumberOfDepartments() {
            return Object.keys(employeesList).length; // Getting the number of departments by counting the keys in employeesList
        }
    };
}