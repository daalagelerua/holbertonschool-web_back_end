export default function createEmployeesObject(departmentName, employees) {
    const departmentKey = `$${departmentName}`;
    return {
        [departmentKey]: employees
    };
}